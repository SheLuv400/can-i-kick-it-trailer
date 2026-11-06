import {Sequence,useVideoConfig} from 'remotion';
import {Base,Plate,Title,Atmosphere,Flash,Insert} from '../design';
import {assets} from '../assets';
export const Finale=()=>{const {fps}=useVideoConfig();return <Base><Sequence durationInFrames={300} premountFor={fps}><Insert src={assets.finale} name="ONE LAST ENCORE" range="01:08–01:18" cue="Low Crowd Meters → Encore → silence → bass drop → victory"/></Sequence><Sequence from={300} durationInFrames={60} premountFor={fps}><Plate/><Title size={180}>THAT’S GAME!</Title><Atmosphere/><Flash/></Sequence><Sequence from={360} durationInFrames={60} premountFor={fps}><Plate zoom={.3}/><Title size={145} top={300}>MAKE<br/>SOME NOISE!</Title><Atmosphere/><Flash/></Sequence></Base>};
